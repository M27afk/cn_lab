import java.net.*;
import java.io.*;
import java.util.*;

public class server{
public static void main(String args[]) throws IOException
{
	ServerSocket ss= new ServerSocket (4999);
	Socket s=ss.accept();
	System.out.println("Client Connected\n");
	
	PrintWriter pr= new PrintWriter(s.getOutputStream());
	pr.write("Hello client");
	pr.flush();
	
	InputStreamReader in = new InputStreamReader(s.getInputStream());
	BufferedReader bf= new BufferedReader(in);
	
	String str=bf.readLine();
	System.out.println("Filename from client: "+str);
	
	File file=new File(str);
	try{
		Scanner openfile= new Scanner(file);
		while(openfile.hasNextLine())
		{
			String filedata=openfile.nextLine();
			System.out.println(filedata);
		}
	openfile.close();
	}
	catch (FileNotFoundException e)
	{
	System.out.println("Does not exist");
	}
	
}
}
