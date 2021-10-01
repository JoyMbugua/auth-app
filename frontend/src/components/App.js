import React, { Component } from "react";
import { Switch, Link, Route } from "react-router-dom";
import EmailSignup from "./EmailSignup";
import PhoneSignup from "./PhoneSignup";
import RegisterPage from "./RegisterPage";
import OTPView from "./Otp";
import Dashboard from "./Dashboard";
import MagicLinkHandler from "./LinkHandler";
import LoginPage from "./LoginPage";
import EmailLogin from "./EmailLogin";
import PhoneLogin from "./PhoneLogin";

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
