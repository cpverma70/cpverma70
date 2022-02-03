package com.api.demo.util;

import java.util.regex.Matcher; 
import java.util.regex.Pattern;

public class CommonUtil {
	
	private static final String regex = "[^-a-zA-Z]";

	public static boolean isValidQuery(String inputString) {
		
		Pattern pattern = Pattern.compile(regex);
	    Matcher matcher = pattern.matcher(inputString);
	    
	  return !matcher.find();
	}

}
