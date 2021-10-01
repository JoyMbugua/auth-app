import React, { Component } from "react";
import { Switch, Link, Route } from "react-router-dom";
import EmailSignup from "./signup/EmailSignup";
import PhoneSignup from "./signup/PhoneSignup";
import RegisterPage from "./signup/RegisterPage";
import OTPView from "./Otp";
import Dashboard from "./views/Dashboard";
import MagicLinkHandler from "./views/LinkHandler";
import LoginPage from "./login/LoginPage";
import EmailLogin from "./login/EmailLogin";
import PhoneLogin from "./login/PhoneLogin";
import Logout from "./views/Logout";

class App extends Component {
  render() {
    return (
      <div className="site">
        <nav>
          <Link className={"nav-link"} to={"/"}>
            Home
          </Link>
          <Link className={"nav-link"} to={"/login/"}>
            Login
          </Link>
          <Link className={"nav-link"} to={"/signup/"}>
            Signup
          </Link>
        </nav>
        <main>
          <Switch>
            <Route exact path={"/signup/"} component={RegisterPage} />
            <Route path={"/login/"} component={LoginPage} />
            <Route path={"/logout/"} component={Logout} />
            <Route exact path={"/email-signup/"} component={EmailSignup} />
            <Route exact path={"/email-login/"} component={EmailLogin} />
            <Route exact path={"/phone-signup/"} component={PhoneSignup} />
            <Route exact path={"/phone-login/"} component={PhoneLogin} />
            <Route exact path={"/verify/"} component={OTPView} />
            <Route exact path={"/dashboard/"} component={Dashboard} />
            <Route exact path={"/verifyemail/"} component={MagicLinkHandler} />
            <Route path={"/"} render={() => <div>Home again</div>} />
          </Switch>
        </main>
      </div>
    );
  }
}
export default App;
