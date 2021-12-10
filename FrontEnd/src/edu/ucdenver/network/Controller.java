package FrontEnd.src.edu.ucdenver.network;

import javafx.animation.TranslateTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.util.Duration;

import java.io.IOException;
import java.net.URL;
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
    private ListView<String> listOfProjects;

    @FXML
    private TextField projectName;

    @FXML
    private Button btnAdd,btnDelete;


    @FXML
    public void addProject(MouseEvent event) {
        listOfProjects.getItems().add(projectName.getText());
    }
    
    @FXML
    public void removeProject(javafx.scene.input.MouseEvent event) {
        int selectedID = listOfProjects.getSelectionModel().getSelectedIndex();
        listOfProjects.getItems().remove(selectedID);
    }




    @Override
    public void initialize(URL url, ResourceBundle resources) {

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
    void handleButtonAction(ActionEvent event) {
        if(event.getSource()==btnAdd){
            showAsDialog("addNew");
        }
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
