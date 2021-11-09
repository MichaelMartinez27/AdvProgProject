package FrontEnd.src.edu.ucdenver.network;

import java.util.Arrays;
import java.util.HashMap;

public class Request {
    private String userUID;
    private String queryAction;
    private String queryElement;
    private String elementUID;
    private String[] filters;
    private HashMap<String,String> requestedInfo;
    private HashMap<String,String> newInfo;

    public Request(String userUID, String queryAction,
                   String queryElement, String elementUID) {
        this.userUID = userUID;
        this.queryAction = queryAction;
        this.queryElement = queryElement;
        this.elementUID = elementUID;
        this.filters = new String[]{};
        this.requestedInfo = new HashMap<>();
        this.newInfo = new HashMap<>();
    }

    public String getUserUID() {
        return userUID;
    }

    public void setUserUID(String userUID) {
        this.userUID = userUID;
    }

    public String getQueryAction() {
        return queryAction;
    }

    public void setQueryAction(String queryAction) {
        this.queryAction = queryAction;
    }

    public String getQueryElement() {
        return queryElement;
    }

    public void setQueryElement(String queryElement) {
        this.queryElement = queryElement;
    }

    public String getElementUID() {
        return elementUID;
    }

    public void setElementUID(String elementUID) {
        this.elementUID = elementUID;
    }

    public String[] getFilters() {
        return filters;
    }

    public void setFilters(String[] filters) {
        this.filters = filters;
    }

    public HashMap<String, String> getRequestedInfo() {
        return requestedInfo;
    }

    public void setRequestedInfo(HashMap<String, String> requestedInfo) {
        this.requestedInfo = requestedInfo;
    }

    public HashMap<String, String> getNewInfo() {
        return newInfo;
    }

    public void setNewInfo(HashMap<String, String> newInfo) {
        this.newInfo = newInfo;
    }

    @Override
    public String toString() {
        return "{" +
                "\"userUID\":\"" + userUID + "\"," +
                "\"queryAction\":\"" + queryAction + "\"," +
                "\"queryElement\":\"" + queryElement + "\"," +
                "\"elementUID\":\"" + elementUID + "\"," +
                "\"filters\":" + Arrays.toString(filters) + ',' +
                "\"requestedInfo\":" + requestedInfo + ',' +
                "\"newInfo\":" + newInfo +
                '}';
    }
}
