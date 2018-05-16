package com.example.a37616.testdemo;


import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.example.a37616.testdemo.MainActivity;

import static org.junit.Assert.assertEquals;

/**
 * Created by 37616 on 2018/5/16.
 */
public class MainActivityTest1 {
    MainActivity myapp = null;
    @Before
    public void setUp() throws Exception{
        
        myapp = new MainActivity();
        System.out.println("初始化...");
    }
    @After
    public void tearDown() throws Exception{
        myapp = null;
        System.out.println("结束了...");
    }
    @Test
    public void addTest1()  {
        assertEquals(myapp.add(2,3),5);
    }

    @Test
    public void addTest2()  {
        assertEquals(myapp.add(2,7),10);
    }
    @Test
    public void addTest3()  {
        assertEquals(myapp.add(22,7),29);
    }
}