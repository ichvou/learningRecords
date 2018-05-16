package com.example.a37616.testdemo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import com.example.a37616.testdemo.MainActivity;

import static org.junit.Assert.*;

/**
 * Created by 37616 on 2018/5/16.
 */
public class MainActivityTest {
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
    public void testAdd() throws Exception {

        System.out.println("开始了...");
        assertEquals(myapp.add(3,2),5);
        assertEquals(myapp.add(1,2),3);
        assertEquals(myapp.add(1,10000),10001);

    }
}