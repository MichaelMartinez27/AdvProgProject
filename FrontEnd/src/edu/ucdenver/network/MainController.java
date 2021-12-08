package FrontEnd.src.edu.ucdenver.network;


import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

import java.lang.reflect.Member;
import java.net.URL;
import java.util.ResourceBundle;

public class MainController implements Initializable {

    @FXML
    private TableView<Member> tbVMembers;

    @FXML
    private TableColumn<Member, String> tcUserName;

    @FXML
    private TableColumn<Member, String> tcFirstName;

    @FXML
    private TableColumn<Member, String> tcEmail;

    @FXML
    private TableColumn<Member, String> tcLastName;


    private ObservableList<Member> data;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        tcFirstName.setCellValueFactory(new PropertyValueFactory<>("First Name"));
        tcLastName.setCellValueFactory(new PropertyValueFactory<>("Last Name"));
        tcUserName.setCellValueFactory(new PropertyValueFactory<>("Username"));
        tcEmail.setCellValueFactory(new PropertyValueFactory<>("Email"));

        data = FXCollections.observableArrayList();
        tbVMembers.setItems(data);
    }
}