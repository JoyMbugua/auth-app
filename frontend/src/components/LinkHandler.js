import React, { Component } from "react";
import axios from "axios";

class MagicLinkHandler extends Component{
    constructor(props){
        super(props);

        this.handleEmail = this.handleEmail.bind(this);
    }
    
    async handleEmail(){
        try {
            await axios
              .post("http://127.0.0.1:8000/api/v1/emaillogin/dashboard/")
              .then((resp) => resp)
              .then((result) => {
                  console.log("Results",result)
                if (result.data.message === "magiclink ok") {
                  localStorage.clear()
                  localStorage.setItem('access_token', result.data.token.access)
                  localStorage.setItem('refresh_token', result.data.token.refresh)
                  window.location.replace('/dashboard/')
                  return result.data           
                } else if(result.data.message === 'wrong email or otp code'){   
                  console.log(result.data.message)
              }
              } 
              )
          } catch (error) {
            console.log(error);
          }
    }
    componentDidMount(){
        this.handleEmail()
    }

    render(){
        return(
            <h3 className="centered-text">Verifying email...</h3>
        )
    }
}

export default MagicLinkHandler;