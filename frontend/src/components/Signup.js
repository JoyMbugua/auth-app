import React, { Component } from "react";
import axios from "axios";
import CSRFToken from "./Csrf";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class Signup extends Component {
  constructor(props) {
    super(props);

    this.state = {
        username: "",
        email: "",
        email2: "",
        emailMismatch: ""
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
      const emailBool = this.state.email === this.state.email2

      if(emailBool){
        await axios
        .post("http://127.0.0.1:8000/api/v1/users/register/", {
          username: this.state.username,
          email: this.state.email,
        })
        .then((res) => res)
        .then((result) => {
          if (result.status === 201) {
            console.log(result);
            window.location.replace("http://127.0.0.1:8000/verify/");
          }
        });
      }else{
          this.setState({
              emailMismatch: "The two password fields didn’t match."
          })
      }
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
            <legend>Sign Up</legend>
            <p className="errormsg">{this.state.emailMismatch}</p>
            <input
              name="username"
              placeholder="Username"
              type="text"
              value={this.state.username}
              onChange={this.handleChange}
            />

            <input
              placeholder="Email Address"
              name="email"
              type="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
            <input
             placeholder="Confirm Email"
            name="email2"
            type="email"
            value={ this.state.email2 }
            onChange={this.handleChange}
            />
            <input type="submit" value="Submit" onClick={this.shareData} />
          </fieldset>
        </form>
      </div>
    );
  }
}

export default Signup;
