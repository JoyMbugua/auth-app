import axios from "axios";
import React, { Component } from "react";
import CSRFToken from "./Csrf";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class OTPView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      otpCode: "",
      error: false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ otpCode: event.target.value });
  }

  async handleSubmit(event) {
    console.log("state", this.state);
    const name = localStorage.getItem('name')
    console.log("name",name)
    event.preventDefault();
    try {
      await axios
        .post("http://127.0.0.1:8000/api/v1/verify/", {
          otpCode: this.state.otpCode,
          username: name
        })
        .then((resp) => resp)
        .then((result) => {
          if (result.data.message === "otp verified") {
            localStorage.clear()
            localStorage.setItem('access_token', result.data.token.access)
            localStorage.setItem('refresh_token', result.data.token.refresh)
            window.location.replace('/dashboard/')
            return result.data           
          } else if(result.data.message === 'wrong otp code'){   
            console.log(result.data.message)
        }
        } 
        )
    } catch (error) {
      console.log(error);
      this.setState({
          error: true
      })
    }
  }

  componentDidMount(){

  }

  render() {
    return (
      <div>
        <form className="otpform" onSubmit={this.handleSubmit}>
          <CSRFToken />
          <label>
            Enter OTP Code:{" "}
            <input name="username" type="text" onChange={this.handleChange} />
          </label>
          <input type="submit" value="Send" />
        </form>
        {this.state.error && <p className="otperror errormsg">Wrong code. Please try again...</p>}
      </div>
    );
  }
}

export default OTPView;
