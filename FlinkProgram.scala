package org.apache.flink.quickstart


import org.apache.flink.api.common.serialization.SimpleStringSchema
import org.apache.flink.streaming.api.scala._
import org.apache.flink.streaming.api.windowing.assigners.GlobalWindows
import org.apache.flink.streaming.api.windowing.triggers.Trigger.TriggerContext
import org.apache.flink.streaming.api.windowing.triggers.{PurgingTrigger, Trigger, TriggerResult}
import org.apache.flink.streaming.api.windowing.windows.{GlobalWindow, Window}


object FlinkProgram {

  def main(args: Array[String]) {


    val count = 0
    val port = 6066

    val env = StreamExecutionEnvironment.getExecutionEnvironment


    //Create streams for names and ages by mapping the inputs to the corresponding objects
    val text = env.socketTextStream("localhost", port, '\n')
    val allValues = text.map {_.split("[,]") filter { _.nonEmpty } }

    val dataTyped:DataStream[(Int,Double,Double,Double,Double)] = allValues.map { x =>
      (1, x(0).toDouble, x(1).toDouble, x(2).toDouble, x(3).toDouble)
    }

    val events:DataStream[Sensor]  = dataTyped
      .map(x => Sensor(x._1, x._2, x._3, x._4, x._5))



    val windowed = events

      .keyBy("stream_num")
      .window(GlobalWindows.create())
      .trigger(PurgingTrigger.of(new MarksTrigger[GlobalWindow]()))
      .sum(1)
      //.apply{x => x.toString}

    windowed.map(x => x.toString)
          .writeToSocket("localhost", 9099, new SimpleStringSchema())

    env.execute("Scala SocketTextStreamWordCount Example")
  }

  class MarksTrigger[W <: Window] extends Trigger[Sensor,W] {

    var count = 0
    override def onElement(element: Sensor, timestamp: Long, window: W, ctx: TriggerContext): TriggerResult = {
      //trigger is fired if average marks of a student cross 80
      if(element.magnitude > 1.5) {
        count = count +1
      }
      if(count >0 && count <= 500)
        {
          if(count < 500)count = count+1
          else count = 0
          TriggerResult.FIRE
        }
      else TriggerResult.CONTINUE
    }

    override def onProcessingTime(time: Long, window: W, ctx: TriggerContext): TriggerResult = {
      TriggerResult.CONTINUE
    }
    override def onEventTime(time: Long, window: W, ctx: TriggerContext): TriggerResult = {
      TriggerResult.CONTINUE
    }

    override def clear(window: W, ctx: TriggerContext) = ???
  }



  case class Sensor(stream_num : Int, X_axis : Double, Y : Double, Z : Double, magnitude : Double)


}

