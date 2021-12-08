package FrontEnd.src.edu.ucdenver.network;

import javafx.beans.property.SimpleStringProperty;

public class Member {
    SimpleStringProperty UserName;
    SimpleStringProperty FirstName;
    SimpleStringProperty LastName;
    SimpleStringProperty Email;

    public Member(String name, String phone, String email, String action) {
        UserName = new SimpleStringProperty();
        FirstName = new SimpleStringProperty(phone);
        LastName = new SimpleStringProperty(email);
        Email = new SimpleStringProperty(action);
    }

    public String getUserName() {
        return UserName.get();
    }

    public void setUserName(String userName) {
        this.UserName.set(userName);
    }

    public String getFirstName() {
        return FirstName.get();
    }

    public void setFirstName(String firstName) {
        this.FirstName.set(firstName);
    }

    public String getLastName() {
        return LastName.get();
    }

    public void setLastName(String email) {
        this.LastName.set(email);
    }

    public String getEmail() {
        return Email.get();
    }

    public void setEmail(String email) {
        this.UserName.set(email);
    }
}
