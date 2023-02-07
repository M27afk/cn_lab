import java.util.*;
import java.net.*;
import java.io.*;

public class client{
public static void main(String args[] )throws IOException{
	Socket s=new Socket("localhost",4999);
	PrintWriter pr= new PrintWriter(s.getOutputStream());
	
	pr.println("file.txt");
	pr.flush();
	InputStreamReader ir= new InputStreamReader(s.getInputStream());
	BufferedReader bf=new BufferedReader(ir);
	
	String str=bf.readLine();
	System.out.println("Server: "+str);
}}
