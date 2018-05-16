package com.example.a37616.testdemo;

//import junit.framework.Test;
//import junit.framework.TestSuite;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
/**
 * Created by 37616 on 2018/5/16.
 */
@RunWith(Suite.class)
@Suite.SuiteClasses({MainActivityTest.class,MainActivityTest1.class})

public class TestSuiteSample  {
//    public static Test suite(){
//        TestSuite testSuite = new TestSuite("test");
//        testSuite.addTestSuite(MainActivityTest.class);
//        testSuite.addTest(TestSuite.createTest(MainActivityTest1.class,"addTest1"));
//        testSuite.addTest(TestSuite.createTest(MainActivityTest1.class,"addTest2"));
//        testSuite.addTest(TestSuite.createTest(MainActivityTest1.class,"addTest3"));
//        return testSuite;
//    }
}
