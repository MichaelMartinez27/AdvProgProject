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
import org.json.JSONArray;

public class Client {
    private final String serverAddress;
    private final int serverPort;
    private PrintWriter writer;
    private InputStreamReader reader;
    private Request request;

    public Client(String serverAddress, int serverPort, Request request) {
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.request = request;
        this.setup();
    }

    private void setup() {
        try {
            Socket socket = new Socket(this.serverAddress, this.serverPort);
            OutputStream output = socket.getOutputStream();
            this.writer = new PrintWriter(output, true);
            InputStream input = socket.getInputStream();
            this.reader = new InputStreamReader(input);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    public JSONArray send(){
        int character;
        StringBuilder data = new StringBuilder();

        System.out.println(this.request);
        this.writer.println(this.request);

        try {
            while ((character = reader.read()) != -1) {data.append((char) character);}
            JSONArray json_array = new JSONArray(data.toString());
            System.out.println(json_array.toString(4));
            return json_array;

        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return null;
    }

    public String getServerIP() {
        return serverAddress;
    }

    public int getServerPort() {
        return serverPort;
    }

    public Request getRequest() {
        return request;
    }

    public void setRequest(Request request) {
        this.request = request;
    }

    static public void main(String[] args) {
        Request request;
        Client c;

        request = new Request("1111","CREATE","USER","1234");
        request.setNewInfo(new HashMap<String,String>(){{
            put("username","hello.world");
            put("password","password123");
            put("firstName","Jordan");
            put("lastName","Correy");
            put("email","hello.world@gmail.com");
            put("admin","True");
        }});
        c = new Client("127.0.0.1", 3920, request);
        c.send();

        request = new Request("1111","CREATE","USER","");
        request.setNewInfo(new HashMap<String,String>(){{
            put("username","newuser");
            put("password","passwd");
            put("firstName","Michael");
            put("lastName","Martinez");
            put("email","foo.bar@gmail.com");
            put("admin","False");
        }});
        c = new Client("127.0.0.1", 3920, request);
        c.send();

        request = new Request("1111","CREATE","USER","");
        request.setNewInfo(new HashMap<String,String>(){{
            put("username","something");
            put("password","abcABC123");
            put("firstName","Sallah");
            put("lastName","Siddiqui");
            put("email","something@email.com");
            put("admin","True");
        }});
        c = new Client("127.0.0.1", 3920, request);
        c.send();


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

        request = new Request("0001","CREATE","PROJECT","001000");
        request.setNewInfo(new HashMap<String,String>(){{
            put("title","ProjectX");
            put("description","New cool project.");
        }});
        c = new Client("127.0.0.1", 3920, request);
        c.send();

        request = new Request("0001","CREATE","THING","54");
        c = new Client("127.0.0.1",3920,request);
        c.send();

        request = new Request("0001","NONACTION","PROJECT","08");
        c = new Client("127.0.0.1",3920,request);
        c.send();

        request = new Request("0001","RETRIEVE","PROJECT","001000-P0001");
        c = new Client("127.0.0.1", 3920, request);
        c.send();

        request = new Request("0003","RETRIEVE","USER","ALL");
        c = new Client("127.0.0.1", 3920, request);
        c.send();
    }
}
