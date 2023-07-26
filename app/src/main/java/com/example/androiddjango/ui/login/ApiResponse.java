package com.example.androiddjango.ui.login;

import com.google.gson.annotations.SerializedName;

public class ApiResponse {
    @SerializedName("message")
    private String message;

    public String getMessage() {
        return message;
    }
}
