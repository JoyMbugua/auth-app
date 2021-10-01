import React, { Component } from "react";
import { Link } from "react-router-dom";

class RegisterPage extends Component {
  render() {
    return (
      <main className="register-site">
        <div className="inputs">
          <Link to={"/email-signup"}>
            <input type="submit" value="Signup with Email" />
          </Link>

          <Link to={"/phone-signup/"}>
            <input type="submit" value="Signup with Phone Number" />
          </Link>
        </div>
      </main>
    );
  }
}
export default RegisterPage;
