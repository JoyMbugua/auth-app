import React, { Component } from "react";
import axios from "axios";
import CSRFToken from "./Csrf";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class EmailLogin extends Component {
  constructor(props) {
    super(props);

    this.state = {
        email: "",
        emailError: false
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
          email: this.state.email,
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
      <div>
        <form onSubmit={this.handleSubmit}>
          <CSRFToken />
          <fieldset>
            <legend>Email Sign Up</legend>
            <p className="errormsg">{this.state.emailError}</p>

            <input
              placeholder="Email Address"
              name="email"
              type="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
           
            <input type="submit" value="Submit" />
          </fieldset>
        </form>
      </div>
    );
  }
}

export default EmailLogin;
