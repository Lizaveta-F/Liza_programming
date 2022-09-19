//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const _ = require("lodash");

const homeStartingContent = "In this space, I am always sharing fresh, flavorful, (mostly) healthy recipes that I love to make and eat in my real, actual, every day life. If I wouldn’t eat it in real life, I won’t put in on the blog. My goal is to inspire you with food that is both approachable AND exciting, whether you’re cooking for yourself, your family, your roommates, or your friends. ";
const aboutContent = "My name is Liza and I am in love with cooking for my loverm especially something tasty and sweet!";
const contactContent = "You can contact me via email: ellizabetta.fadeeva@gmail.com";
let posts =[];

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/", function(req,res){
  
  res.render("home", {
    startingContent:homeStartingContent,
    allposts:posts
  });
})

app.get("/about", function(req,res){
  
  res.render("about", {about:aboutContent});
})

app.get("/contact", function(req,res){
  
  res.render("contact", {contact:contactContent});
})

app.get("/compose", function(req,res){
  
  res.render("compose");
})

app.get("/posts/:postName",function(req,res){
  const requestedTitle = _.lowerCase(req.params.postName);

  posts.forEach(function(post){
    const storedTitle = _.lowerCase(post.title);

    if (storedTitle === requestedTitle)
    {
    const titleName = post.title;
    const contentText = post.content;
    res.render("post", {title:titleName,content:contentText});
  };
});
})

app.post("/compose",function(req,res){
  const post = {
    title:req.body.composition,
    content:req.body.textofPost
  }; 
  posts.push(post);
  res.redirect("/")
});












app.listen(3000, function() {
  console.log("Server started on port 3000");
});
