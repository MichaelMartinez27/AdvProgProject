package FrontEnd.src.edu.ucdenver.network;

import javafx.animation.TranslateTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.io.IOException;
import java.lang.reflect.Member;
import java.net.URL;
import java.util.HashMap;
import java.util.ResourceBundle;

public class Controller implements Initializable {

    @FXML
    private ImageView Exit;

    @FXML
    private Label Menu;

    @FXML
    private Label MenuClose;

    @FXML
    private AnchorPane slider;

    @FXML
    private Label MenuBack;

    @FXML
    private TableView<?> tableView;

    @FXML
    private TableColumn<Client, String> tcUserName;//comes from client

    @FXML
    private TableColumn<Client, String> tcFirstName;

    @FXML
    private TableColumn<Client, String> tcLastName;

    @FXML
    private TableColumn<Client, String> tcEmail;


    @FXML
    private TextField userNameInput;

    @FXML
    private TextField firstNameInput;

    @FXML
    private TextField lastNameInput;

    @FXML
    private TextField emailInput;

    @FXML
    private ListView<String> listOfProjects;

    @FXML
    private TextField projectName;

    @FXML
    private ListView<String> listOfOrganizations;

    @FXML
    private TextField organizationName;

    @FXML
    private Button btnAdd,btnDelete;


    @FXML
    private Button createAccount;

    @FXML
    private Button loginBtn;

    @FXML
    private TextField createPasswordP;

    @FXML
    private TextField emailP;

    @FXML
    private TextField firstNameP;

    @FXML
    private TextField lastNameP;

    @FXML
    private Button updateUserP;

    @FXML
    private TextField userNameP;

    @FXML
    private AnchorPane loginPane;

    @FXML
    private PasswordField loginPassword;

    @FXML
    private ComboBox loginType;

    @FXML
    private TextField loginUserName;

    @FXML
    private TextField signUpEmail;

    @FXML
    private TextField signUpFirstName;

    @FXML
    private TextField signUpLastName;

    @FXML
    private TextField wrongLogin;

    @FXML
    private AnchorPane signUpPane;

    @FXML
    private TextField signUpPassword;

    @FXML
    private ComboBox signUpType;

    @FXML
    private ComboBox addType;

    @FXML
    private TextField signUpUserName;

    public  void LoginPaneShow(){

        loginPane.setVisible(true);
        signUpPane.setVisible(false);
    }

    public  void SignupPaneShow(){

        loginPane.setVisible(false);
        signUpPane.setVisible(true);
    }

    public  void loginUser(ActionEvent event) throws IOException{
        checkLogin();
    }

    public  void createAccount(ActionEvent event) throws IOException{

        Request request3 = new Request("1111","CREATE","USER","");
        request3.setNewInfo(new HashMap<String,String>(){{
            put("username",String.valueOf(signUpUserName));
            put("password",String.valueOf(signUpPassword));
            put("firstName",String.valueOf(signUpFirstName));
            put("lastName",String.valueOf(signUpLastName));
            put("email",String.valueOf(signUpEmail));
            put("admin",String.valueOf(signUpType));
        }});
        Client c1_3 = new Client("127.0.0.1", 3920, request3);
        c1_3.send();
    }


    private  void checkLogin() throws IOException{
        MainGui mainGui = new MainGui();
        Request request = new Request("0003", "RETRIEVE", "USER", "ALL");
        Client c = new Client("127.0.0.1", 3920, request);
        c.send();
        if(loginUserName.getText().equals(String.valueOf(loginUserName)) && loginPassword.getText().equals(String.valueOf(loginPassword)) && loginType.equals(String.valueOf(loginType))){
            wrongLogin.setText("Success!!");

        }

        else if(loginUserName.getText().isEmpty() && loginPassword.getText().isEmpty()){
            wrongLogin.setText("Please enter your credentials!");
        }

        else {
            wrongLogin.setText("Wrong username or password!");
        }
    }

    private void updateUserP (ActionEvent event) throws IOException{
        Request request3 = new Request("1111","UPDATE","USER","");
        request3.setNewInfo(new HashMap<String,String>(){{
            put("username",String.valueOf(userNameP));
            put("password",String.valueOf(createPasswordP));
            put("firstName",String.valueOf(firstNameP));
            put("lastName",String.valueOf(lastNameP));
            put("email",String.valueOf(emailP));
        }});
        Client c1_3 = new Client("127.0.0.1", 3920, request3);
        c1_3.send();
    }


    @Override
    public void initialize(URL url, ResourceBundle resources) {

        loginType.getItems().addAll("Admin","Member");
        signUpType.getItems().addAll("Admin","Member");
        addType.getItems().addAll("Admin","Member");


        tcUserName.setCellValueFactory(new PropertyValueFactory<Client,String>(String.valueOf(userNameInput)));
        tcFirstName.setCellValueFactory(new PropertyValueFactory<Client,String>(String.valueOf(firstNameInput)));
        tcLastName.setCellValueFactory(new PropertyValueFactory<Client,String>(String.valueOf(lastNameInput)));
        tcEmail.setCellValueFactory(new PropertyValueFactory<Client,String>(String.valueOf(emailInput)));
        tcEmail.setCellValueFactory(new PropertyValueFactory<Client,String>(String.valueOf(addType)));

        Exit.setOnMouseClicked(event -> {
            System.exit(0);
        });
        slider.setTranslateX(-176);
        Menu.setOnMouseClicked(event -> {
            TranslateTransition slide = new TranslateTransition();
            slide.setDuration(Duration.seconds(0.4));
            slide.setNode(slider);

            slide.setToX(0);
            slide.play();

            slider.setTranslateX(-176);

            slide.setOnFinished((ActionEvent e)-> {
                Menu.setVisible(false);
                MenuClose.setVisible(true);
            });
        });

        MenuClose.setOnMouseClicked(event -> {
            TranslateTransition slide = new TranslateTransition();
            slide.setDuration(Duration.seconds(0.4));
            slide.setNode(slider);

            slide.setToX(-176);
            slide.play();

            slider.setTranslateX(0);

            slide.setOnFinished((ActionEvent e)-> {
                Menu.setVisible(true);
                MenuClose.setVisible(false);
            });
        });
    }

    @FXML
    public void addProject(MouseEvent event)
    {
        listOfProjects.getItems().add(projectName.getText());
        Request request = new Request("0001", "CREATE", "PROJECT", "001000");
        request.setNewInfo(new HashMap<String,String>(){{
            put("title",String.valueOf(projectName));
        }});
        Client c = new Client("127.0.0.1", 3920, request);
        c.send();
    }

    @FXML
    public void removeProject(javafx.scene.input.MouseEvent event) {
        int selectedID = listOfProjects.getSelectionModel().getSelectedIndex();
        listOfProjects.getItems().remove(selectedID);
        Request request = new Request("0001", "DELETE", "PROJECT", "001000");
        request.setNewInfo(new HashMap<String,String>());
            Client c = new Client("127.0.0.1", 3920, request);
            c.send();
        }

    @FXML
    public void addOrganization(MouseEvent event)
    {
        listOfOrganizations.getItems().add(organizationName.getText());
        Request request = new Request("0001", "CREATE", "ORGANIZATION", "");
        request.setNewInfo(new HashMap<String,String>(){{
            put("name",String.valueOf(organizationName));
        }});
        Client c = new Client("127.0.0.1", 3920, request);
        c.send();
    }

    @FXML
    public void removeOrganization(MouseEvent event)
    {
        int selectedID = listOfOrganizations.getSelectionModel().getSelectedIndex();
        listOfOrganizations.getItems().remove(selectedID);
        Request request = new Request("0001", "DELETE", "ORGANIZATION", "");
        request.setNewInfo(new HashMap<String,String>());
        Client c = new Client("127.0.0.1", 3920, request);
        c.send();
    }


    //Addbutton on admins/members
    @FXML
    void handleButtonAdd(ActionEvent event) {
        if(event.getSource()==btnAdd){
            showAsDialog("addNew");
            Request request1 = new Request("1111","ADD","USER"," ");
            request1.setNewInfo(new HashMap<String,String>(){{
                put("username", String.valueOf(userNameInput));
                put("firstName",String.valueOf(firstNameInput));
                put("lastName",String.valueOf(lastNameInput));
                put("email",String.valueOf(emailInput));
            }});
            Client c1_1 = new Client("127.0.0.1", 3920, request1);
            c1_1.send();

        }
    }
//Delete users
    @FXML
    void handleButtonDelete(ActionEvent event){
        int selectedID = tableView.getSelectionModel().getSelectedIndex();
        tableView.getItems().remove(selectedID);
        Request request1 = new Request(" ","DELETE","USER"," ");
        Client c1_1 = new Client("127.0.0.1", 3920, request1);
        c1_1.send();
    }


    private void showAsDialog(String fxml)
    {
            try
            {
                Parent parent = FXMLLoader.load(getClass().getResource("/fxml/"+fxml+".fxml"));
                Stage stage = new Stage();
                Scene scene = new Scene(parent);
                stage.setScene(scene);
                stage.show();


            } catch (IOException e)
            {
                e.printStackTrace();
            }
    }

}
