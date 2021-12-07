package FrontEnd.src.edu.ucdenver.network;
/*
 * Project: Project Management Tool
 * Team:    4
 * Author:  Michael Martinez
 * Course:  CSCI 3920
 *
 */

import java.io.*;
import java.net.Socket;
import java.util.HashMap;

public class Client {
    private final String server_address;
    private final int server_port;
    private PrintWriter writer;
    private InputStreamReader reader;
    private Request request;

    public Client(String server_address, int server_port, Request request) {
        this.server_address = server_address;
        this.server_port = server_port;
        this.request = request;
        this.setup();
    }

    private void setup() {
        try {
            Socket socket = new Socket(this.server_address, this.server_port);
            OutputStream output = socket.getOutputStream();
            this.writer = new PrintWriter(output, true);
            InputStream input = socket.getInputStream();
            this.reader = new InputStreamReader(input);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void send(){
        int character;
        StringBuilder data = new StringBuilder();

        System.out.println(this.request);
        this.writer.println(this.request);

        try {
            while ((character = reader.read()) != -1) {data.append((char) character);}
            System.out.println(data);

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    public String getServer_address() {
        return server_address;
    }

    public int getServer_port() {
        return server_port;
    }

    public Request getRequest() {
        return request;
    }

    public void setRequest(Request request) {
        this.request = request;
    }

    static public void main(String[] args) {
        Request request1 = new Request("1111","CREATE","USER","1234");
        request1.setNewInfo(new HashMap<String,String>(){{
            put("username","hello.world");
            put("password","password123");
            put("firstName","Jordan");
            put("lastName","Correy");
            put("email","hello.world@gmail.com");
            put("admin","True");
        }});
        Client c1_1 = new Client("127.0.0.1", 3920, request1);
        c1_1.send();

        Request request2 = new Request("1111","CREATE","USER","");
        request2.setNewInfo(new HashMap<String,String>(){{
            put("username","newuser");
            put("password","passwd");
            put("firstName","Michael");
            put("lastName","Martinez");
            put("email","foo.bar@gmail.com");
            put("admin","False");
        }});
        Client c1_2 = new Client("127.0.0.1", 3920, request2);
        c1_2.send();

        Request request3 = new Request("1111","CREATE","USER","");
        request3.setNewInfo(new HashMap<String,String>(){{
            put("username","something");
            put("password","abcABC123");
            put("firstName","Sallah");
            put("lastName","Siddiqui");
            put("email","something@email.com");
            put("admin","True");
        }});
        Client c1_3 = new Client("127.0.0.1", 3920, request3);
        c1_3.send();

        Request request;
        Client c;
        request = new Request("0001","CREATE","ORGANIZATION","");
        request.setNewInfo(new HashMap<String,String>(){{
            put("name","Pythonia");
        }});
        c = new Client("127.0.0.1", 3920, request);
        c.send();


        request = new Request("0002","CREATE","ORGANIZATION","");
        request.setNewInfo(new HashMap<String,String>(){{
            put("name","JavaComp");
        }});
        c = new Client("127.0.0.1", 3920, request);
        c.send();


        request = new Request("0001","CREATE","PROJECT","");
        request.setNewInfo(new HashMap<String,String>(){{
            put("title","ProjectX");
            put("description","New cool project.");
        }});
        c = new Client("127.0.0.1", 3920, request);
        c.send();


        Client c2 = new Client("127.0.0.1", 3920, request);
        c2.send();

        request = new Request("0001","CREATE","THING","54");
        Client c3 = new Client("127.0.0.1",3920,request);
        c3.send();

        request = new Request("0001","NONACTION","PROJECT","08");
        Client c4 = new Client("127.0.0.1",3920,request);
        c4.send();
        request = new Request("0001","RETRIEVE","project","P0001");
        c = new Client("127.0.0.1", 3920, request);
        c.send();
    }

}
