using MbientLab.MetaWear;
using MbientLab.MetaWear.Core;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Devices.Bluetooth;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;
using System.Net.Sockets;
using System.Net;
using System.Text;
using Windows.Networking;
using Windows.Networking.Sockets;



// The Blank Page item template is documented at https://go.microsoft.com/fwlink/?LinkId=234238

namespace StarterApp {
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class DeviceSetup : Page {
        private IMetaWearBoard metawear;
        TcpClient client;

        public DeviceSetup() {
            InitializeComponent();
        }

        protected override void OnNavigatedTo(NavigationEventArgs e) {
            base.OnNavigatedTo(e);

            metawear = MbientLab.MetaWear.Win10.Application.GetMetaWearBoard(e.Parameter as BluetoothLEDevice);
        }

        private void back_Click(object sender, RoutedEventArgs e) {
            if (!metawear.InMetaBootMode) {
                metawear.TearDown();
                metawear.GetModule<IDebug>().DisconnectAsync();
            }
            Frame.GoBack();
        }
        private async void accStart_Click(object sender, RoutedEventArgs e)
        {
            var accelerometer = metawear.GetModule<MbientLab.MetaWear.Sensor.IAccelerometer>();

            accelerometer.Configure(odr: 25f, range: 2f);

            System.Diagnostics.Debug.WriteLine("Accelerometer configured!");

        
            try
            { 
            client = new TcpClient("127.0.0.1", 6066);

            NetworkStream stream = client.GetStream();
            BinaryWriter w = new BinaryWriter(stream);
                ASCIIEncoding asen = new ASCIIEncoding();

                System.Diagnostics.Debug.WriteLine("Accelerometer configured!");

            await accelerometer.Acceleration.AddRouteAsync(source => source.Stream(data =>
                stream.Write(asen.GetBytes(data.Value<MbientLab.MetaWear.Data.Acceleration>().ToString()),0, asen.GetByteCount(data.Value<MbientLab.MetaWear.Data.Acceleration>().ToString()))
                ));

            accelerometer.Acceleration.Start();
            accelerometer.Start();

        }
            catch (Exception error)
            {
                System.Diagnostics.Debug.WriteLine(error.ToString());
            }


            finally
            {
                System.Diagnostics.Debug.WriteLine("Done");
            }
            
        }
        private void accStop_Click(object sender, RoutedEventArgs e)
        {
            var accelerometer = metawear.GetModule<MbientLab.MetaWear.Sensor.IAccelerometer>();
            client.Close();

            accelerometer.Stop();
            accelerometer.Acceleration.Stop();
            metawear.TearDown();
        }
        static public string ToReadableByteArray(byte[] bytes)
        {
            return string.Join(", ", bytes);
        }



    }
}
