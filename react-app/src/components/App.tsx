import React from "react";
import { CssBaseline } from "@material-ui/core";
import { AppProvider } from "../contexts";

import Navbar from "./nav-bar/Navbar";
import SplitPanes from "./split-panes/SplitPanes";

const App: React.FC = () => {
  return (
    <AppProvider>
      <CssBaseline />

      <Navbar />
      <SplitPanes />
    </AppProvider>
  );
};

export default App;
