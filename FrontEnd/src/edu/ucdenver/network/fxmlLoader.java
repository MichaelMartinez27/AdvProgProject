package FrontEnd.src.edu.ucdenver.network;

import javafx.fxml.FXMLLoader;
import javafx.scene.layout.Pane;

import java.net.URL;

public class fxmlLoader {
private Pane view;


public Pane getPage(String fileName){

    try{
        URL fileUrl = MainGui.class.getResource("/FrontEnd.src.edu.ucdenver.network/" + fileName + ".fxml");
        if (fileUrl  == null){
            throw new java.io.FileNotFoundException("FXML file can't be found");
        }

        view = new FXMLLoader().load(fileUrl);


    }catch (Exception e){
        System.out.println("No page" + fileName + "please check FxmlLoader.");
    }
    return view;
}
}
