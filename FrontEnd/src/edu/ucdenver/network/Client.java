package FrontEnd.src.edu.ucdenver.network;

import java.io.*;
import java.net.*;
import java.util.HashMap;

import static javax.swing.UIManager.put;

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
        Request request = new Request("1","CREATE","USER","1234");
        request.setNewInfo(new HashMap<String,String>(){{
            put("username","hello.world");
            put("first","Michael");
            put("last","Martinez");
            put("email","foo.bar@gmail.com");
        }});
        Client c1 = new Client("127.0.0.1", 3920, request);
        c1.send();















        request = new Request("1","CREATE","ORGANIZATION","6713234");
        request.setNewInfo(new HashMap<String,String>(){{
            put("name","Pythonia");
        }});
        Client c2 = new Client("127.0.0.1", 3920, request);
        c2.send();
        request = new Request("1","CREATE","THING","54");
        Client c3 = new Client("127.0.0.1",3920,request);
        c3.send();
        request = new Request("1","ELEMENT","PROJECT","08");
        Client c4 = new Client("127.0.0.1",3920,request);
        c4.send();
//        request = new Request("2","UPDATE","project","2347980");
//        Client c4 = new Client("127.0.0.1",3920,request);
//        c4.send();
    }

}
