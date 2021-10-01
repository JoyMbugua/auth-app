import React, { Component } from "react";
import axios from "axios";
import CSRFToken from "../Csrf";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class PhoneLogin extends Component {
  constructor(props) {
    super(props);

    this.state = {
        phone: "",
        phoneError: false
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
  
        await axios
        .post("http://127.0.0.1:8000/api/v1/users/login/", {
          phone_number: this.state.phone,
        })
        .then((res) => res)
        .then((result) => {
            console.log("results",result)
          if (result.data.status === 201) {
            console.log(result);
            localStorage.setItem("name",result.data.userdata)
            window.location.replace("http://127.0.0.1:8000/verify/");
          }
        });
    } catch (error) {
      console.log(error.stack);
      this.setState({
        errors: error.response.data,
      });
    }
  }
  render() {
    return (
      <main>
         
        <form id="loginform" onSubmit={this.handleSubmit}>
        <h3 className="centered-text text">Sign In with phone number</h3>
          <CSRFToken />
            <p className="errormsg">{this.state.phoneError}</p>

            <input
              placeholder="Phone Number"
              name="phone"
              type="phone"
              value={this.state.phone}
              onChange={this.handleChange}
            />
           
            <input type="submit" value="Submit" />
        </form>
      </main>
    );
  }
}

export default PhoneLogin;
