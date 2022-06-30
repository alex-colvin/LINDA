import React from "react";
import { Component } from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";
import useCustomForm from "../../hooks/useCustomForm";

import axios from "axios";

const HomePage = () => {
  // The "user" value from this Hook contains the decoded logged in user information (username, first name, id)
  // The "token" value is the JWT token that you will send in the header of any request requiring authentication
  //TODO: Add an AddCars Page to add a car for a logged in user's garage
  const currentDate = new Date();
  const formattedDate = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`
  const [user, token] = useAuth();
  const [posts, setPosts] = useState([]);


  useEffect(() => {
    const fetchPosts = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/posts/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setPosts(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchPosts();
  }, [token]);

  async function sendPost(id) {
    let response = await axios.get(`http://127.0.0.1:8000/api/posts/link/${id}/`,{
      headers: {
        Authorization: "Bearer " + token,
      },
    })
    if(response.status == 200){
      console.log(`test response: ${response}`)
      alert('Posted to LinkedIn')
    }
  }

  return (
    <div className="container">
      <h1>Scheduled Posts for {user.first_name}!</h1>
      {posts &&
        posts.map((post) => (
          <p key={post.id}>
            <span>Post Text: {post.post}</span>
            <span>Post Date: {post.date}</span>
            <button onClick={() => sendPost(post.id)}>Post to linkedin</button>
          </p>
        ))}
    </div>
  );
};

export default HomePage;
