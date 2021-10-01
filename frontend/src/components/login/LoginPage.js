import React, { Component } from "react";
import { Link } from "react-router-dom";

class LoginPage extends Component {
  render() {
    return (
      <main className="login-site">
        <div className="inputs">
          <Link to={"/email-login"}>
            <input type="submit" value="Login with Email" />
          </Link>

          <Link to={"/phone-login/"}>
            <input type="submit" value="Login with Phone Number" />
          </Link>
        </div>
      </main>
    );
  }
}
export default LoginPage;
