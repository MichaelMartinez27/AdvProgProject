package FrontEnd.src.edu.ucdenver.network;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

import java.io.IOException;

public class MainGui extends Application {
    double x,y = 0;
    @Override
    public void start(Stage stage) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("FrontEnd.src.edu.ucdenver.network.fxml"));
        Scene scene = new Scene(root);
        stage.initStyle(StageStyle.UNDECORATED);

       /*
        FXMLLoader fxmlLoader = new FXMLLoader(MainGui.class.getResource("gui.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 850, 523);
        stage.setScene(scene);
        stage.show();
        */

        root.setOnMousePressed(event -> {
            x = event.getSceneX();
            y = event.getSceneY();
        });

        root.setOnMouseDragged(event -> {
            stage.setX(event.getScreenX() - x);
            stage.setY(event.getScreenY() - y);
        });
        stage.setScene(scene);
        stage.show();
    }

        public static void main (String[]args){
            launch();
        }

}