import React, { Component } from "react";
import axios from "axios";
import CSRFToken from "../Csrf";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class PhoneSignup extends Component {
  constructor(props) {
    super(props);

    this.state = {
        username: "",
        phoneNumber: "",
        phoneNumber2: "",
        phoneNumberMismatch: false,
        formerrors: false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ [event.target.name]: event.target.value });
  }

  async handleSubmit(event) {
    event.preventDefault();
    try {
      const phoneNumberBool = this.state.phoneNumber === this.state.phoneNumber2

      if(phoneNumberBool){
         
        await axios
        .post("http://127.0.0.1:8000/api/v1/users/register/", {
          username: this.state.username,
          phone_number: this.state.phoneNumber,
        })
        .then((res) => res)
        .then((result) => {
          if (result.status === 201) {
            
            localStorage.setItem("name",this.state.username)
            window.location.replace("http://127.0.0.1:8000/verify/");
          }
        });
      }else{
          this.setState({
              phoneNumberMismatch: true
          })
      }
    } catch (error) {
      console.log(error.stack);
     if(error){
        this.setState({
            formerrors: true,
          });
     }
    }
  }
  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
           {this.state.formerrors && (
               <p className="errormsg">
                   Incorrect form inputs!
               </p>
           )}
           <br />
          <CSRFToken />
          <fieldset>
            <legend>Phone Sign Up</legend>
            {this.state.phoneNumberMismatch && (
                <p className="errormsg">The two phone number fields didn’t match!</p>
            )}
            <input
              name="username"
              placeholder="Username"
              type="text"
              value={this.state.username}
              onChange={this.handleChange}
            />
            <input
              placeholder="Phone Number e.g +234711233455"
              name="phoneNumber"
              value={this.state.phoneNumber}
              onChange={this.handleChange}
            />
            <input
             placeholder="Confirm Phone Number"
            name="phoneNumber2"
            value={ this.state.phoneNumber2 }
            onChange={this.handleChange}
            />
            <input type="submit" value="Submit" />
          </fieldset>
        </form>
      </div>
    );
  }
}

export default PhoneSignup;
