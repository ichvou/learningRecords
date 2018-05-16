package com.example.a37616.testdemo;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.R.string;
import android.app.Activity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    public int add(int num1, int num2){
        return num1 + num2;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button calc = (Button)findViewById(R.id.btncalc);
        calc.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText t1 = (EditText)findViewById(R.id.edtnum1);
                EditText t2 = (EditText)findViewById(R.id.edtnum2);

                int a = Integer.parseInt(t1.getText().toString());
                int b = Integer.parseInt(t2.getText().toString());
                String s = Integer.toString(add(a, b));
                Toast.makeText(MainActivity.this, s, Toast.LENGTH_LONG).show();
            }
        });
        Button exit = (Button)findViewById(R.id.btnexit);
        exit.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu){
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

/*    @Override
    public boolean onOptionsItemSelected(MenuItem item){
        int id = item.getItemId();
        if(id == R.id.action_settings){
            return true;
        }
        return super.onOptionsItemSelected(item);
    }*/
}

