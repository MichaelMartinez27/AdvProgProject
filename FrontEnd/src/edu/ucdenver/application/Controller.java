package FrontEnd.src.edu.ucdenver.application;

import FrontEnd.src.edu.ucdenver.application.MainGui;
import FrontEnd.src.edu.ucdenver.network.Client;
import FrontEnd.src.edu.ucdenver.network.Request;
import FrontEnd.src.edu.ucdenver.network.fxmlLoader;
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
import javafx.scene.layout.Pane;
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
    private BorderPane mainPane;

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

    //This is to switch scenes when the profile button is clicked
    @FXML
    private void handleButtonProfile(ActionEvent event){
        fxmlLoader object = new fxmlLoader();
        Pane view = object.getPage("Profile");
        mainPane.setCenter(view);
    }
    //This is to switch scenes when the Users button is clicked
    @FXML
    private void handleButtonUsers(ActionEvent event){
        fxmlLoader object = new fxmlLoader();
        Pane view = object.getPage("Users");
        mainPane.setCenter(view);
    }
    //This is to switch scenes when the Projects button is clicked
    @FXML
    private void handleButtonProjects(ActionEvent event){
        fxmlLoader object = new fxmlLoader();
        Pane view = object.getPage("Projects");
        mainPane.setCenter(view);
    }
    //This is to switch scenes when the Organizations button is clicked
    @FXML
    private void handleButtonOrganizations(ActionEvent event){
        fxmlLoader object = new fxmlLoader();
        Pane view = object.getPage("Organizations");
        mainPane.setCenter(view);
    }

//This is for the login button
    public  void LoginPaneShow(){

        loginPane.setVisible(true);
        signUpPane.setVisible(false);
    }
//This is for the signup button
    public  void SignupPaneShow(){

        loginPane.setVisible(false);
        signUpPane.setVisible(true);
    }

//This is to create a new user
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


//This is to check if the login credentials are correct
    public  void loginUser(ActionEvent event) throws IOException{
        checkLogin();
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


//This is to update user profile
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
//This is to add projects
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
//This is to remove projects
    @FXML
    public void removeProject(javafx.scene.input.MouseEvent event) {
        int selectedID = listOfProjects.getSelectionModel().getSelectedIndex();
        listOfProjects.getItems().remove(selectedID);
        Request request = new Request("0001", "DELETE", "PROJECT", "001000");
        request.setNewInfo(new HashMap<String,String>());
            Client c = new Client("127.0.0.1", 3920, request);
            c.send();
        }

    //This is to add Organizations
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
    //This is to Delete Organizations
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


    //This is to add new member/admin
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
                put("Type",String.valueOf(addType));
            }});
            Client c1_1 = new Client("127.0.0.1", 3920, request1);
            c1_1.send();

        }
    }

//This is to delete member/admin
    @FXML
    void handleButtonDelete(ActionEvent event){
        int selectedID = tableView.getSelectionModel().getSelectedIndex();
        tableView.getItems().remove(selectedID);
        Request request1 = new Request(" ","DELETE","USER"," ");
        Client c1_1 = new Client("127.0.0.1", 3920, request1);
        c1_1.send();
    }

//This is dialog box for add new member/admin
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
