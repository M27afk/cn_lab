import java.util.*;
import java.io.*;
import java.net.*;

public class server{
	public static void main(String args[]) throws IOException{
		DatagramSocket ds= new DatagramSocket();
		InetAddress client = InetAddress.getByName("127.0.0.1");
		DatagramPacket dp;
		String msg;
		byte[] buffer;
		Scanner in = new Scanner(System.in);
		System.out.println("Enter msg:");
		while(true){
				msg=in.nextLine();
				buffer=msg.getBytes();
				dp=new DatagramPacket(buffer,buffer.length,client,4000);
				ds.send(dp);
				
				if(msg.equalsIgnoreCase("bye")){
					ds.close();
					break;				
				}					
		}	
	}
}
