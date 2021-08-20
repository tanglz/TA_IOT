package com.example.iot;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Context;
import android.net.wifi.ScanResult;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.widget.TextView;

import java.util.Date;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        List<ScanResult> wifiList = wifiManager.getScanResults();
        for (int i=0; i<wifiList.size(); i++) {
            String sp = wifiList.get(i).SSID;
            String signal = Integer.toString(wifiList.get(i).level);
            String  bssid = wifiList.get(i).BSSID;
            String date = new Date().toString();
        }
        WifiInfo wfInfo = wifiManager.getConnectionInfo();
        String currentSsid = wfInfo.getSSID();
        setContentView(R.layout.activity_main);
        TextView textView = findViewById(R.id.textView1);
        textView.setText(currentSsid);
    }

}