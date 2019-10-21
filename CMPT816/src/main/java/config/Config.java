/*
 * Author: C M Khaled Saifullah
 * nsid: cms500
 * Assignment for CMPT470/816
 */

package config;

import java.util.ArrayList;
import java.util.Arrays;

public class Config {
    private static final String ROOT_PATH = "./";
    public static final String REPOSITORY_PATH = ROOT_PATH+"data/repository/";
    public static final String DATSET_PATH = ROOT_PATH+"data/dataset/";
    public static final String LOG_PATH = ROOT_PATH+"cms500_codeparser.log";
    public static final int THREAD_POOL_SIZE = 8;


    private static final String[] PACKAGE_NAME ={"java"};
    public static final String DATASET_HEAD ="FilePath,LineNumber,RecieverVaribale,Context,Label\n";

    public static final ArrayList<String> JAVA_KEYWORDS = new ArrayList<>(Arrays.asList("abstract","boolean","break","byte",
            "case","catch","char","class","const","continue", "default","do","double","else","extends","final","finally","float",
            "for","goto","if","implements","import","instanceof","int","interface","long","native","new","null","package","private",
            "protected","public","return","short","static","super","switch","synchronized","this","throw","throws","transient","try",
            "void","volatile","while","assert","enum","strictfp","null","true","false","=","<","<=",">",">=","=="));



    public static final boolean isAllowedPackage(String packagename) {
        if(packagename == null)
                return false;

        for(String each_package: PACKAGE_NAME)
            if (packagename.trim().startsWith(each_package))
                return true;

        return false;
    }
}
