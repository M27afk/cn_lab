
import java.util.*;
import java.net.*;
import java.io.*;

public class client{
	public static void main(String[] args) throws IOException{
		Scanner in = new Scanner(System.in);
		DatagramSocket ds = new DatagramSocket(4000);
		byte[] buffer;
		DatagramPacket dp;
		System.out.println("Received: ");
		while(true){
			buffer = new byte[65553];
			dp=new DatagramPacket(buffer,buffer.length);
			ds.receive(dp);
			String rec=new String(buffer).trim();
			System.out.println(rec);
			if(rec.equalsIgnoreCase("bye")){
				ds.close();
				break;			
			}		
		}	
	}
}
