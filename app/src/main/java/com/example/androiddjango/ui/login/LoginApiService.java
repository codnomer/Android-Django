package com.example.androiddjango.ui.login;

import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;

import com.google.gson.annotations.SerializedName;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;


public interface LoginApiService {

    @POST("loginpage/login/")
    Call<ApiResponse> loginUser(@Body LoginRequest loginRequest);
}

