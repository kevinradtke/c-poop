import React, { useContext } from "react";
import axios from "axios";

import { AppBar, Button, Toolbar, Typography } from "@material-ui/core/";
import { TranslatedContext } from "../../contexts/translatedContext";
import { TerminalContext } from "../../contexts/terminalContext";
import { TabsContext } from "../../contexts/tabsContext";
import { CodeContext } from "../../contexts/codeContext";

import useStyles from "./navbar.jss";

const Navbar: React.FC = () => {
  const classes = useStyles();

  const { handleTranslation } = useContext(TranslatedContext);
  const { handleTerminal } = useContext(TerminalContext);
  const { handleChangeIndex } = useContext(TabsContext);
  const { ref } = useContext(CodeContext);

  const handleResetServer = () => {
    axios.get("http://localhost:5000/reset");
    const { editor } = ref.current;
    editor.focus();
  };

  return (
    <div className={classes.root}>
      <AppBar position="static" elevation={2} className={classes.appbar}>
        <Toolbar>
          <Typography variant="h5" className={classes.title}>
            {"C"}
            <span role="img" aria-label="title-poop-emoji">
              {"💩 "}
            </span>
            {"Compiler"}
          </Typography>
          <Button
            variant="outlined"
            onClick={() => handleResetServer()}
            className={classes.reset}
          >
            Reset Server
          </Button>
          <Button
            variant="outlined"
            onClick={() => {
              handleTranslation();
              handleChangeIndex(0);
            }}
            className={classes.translateButton}
          >
            Translate
          </Button>
          <Button
            variant="outlined"
            color="secondary"
            onClick={() => {
              handleTerminal();
              handleChangeIndex(1);
            }}
          >
            Run
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default Navbar;
