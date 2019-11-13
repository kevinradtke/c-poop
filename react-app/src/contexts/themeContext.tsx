import React, { createContext } from "react";
import { createMuiTheme, MuiThemeProvider } from "@material-ui/core/styles";
import { grey } from "@material-ui/core/colors";

const fetchTheme = localStorage.getItem("theme");
const fetchFontSize = Number(localStorage.getItem("fontSize"));

type ContextProps = {
  type: "light" | "dark";
  fontSize: number;
  options: {
    type: string[];
    fontSize: number[];
  };
};

const initialState: ContextProps = {
  type: fetchTheme === "light" ? "light" : "dark",
  fontSize: fetchFontSize || 14,
  options: {
    type: ["light", "dark"],
    fontSize: [12, 14, 16, 18]
  }
};

// const codeAcademyColors = {
//   light: "#1f1e2e",
//   main: "#15141f",
//   dark: "#111019"
// };

const ThemeContext = createContext(initialState);

const ThemeProvider = ({ children }: { children: any }) => {
  const { type, fontSize } = initialState;

  const muitheme = createMuiTheme({
    palette: {
      type,
      primary: {
        light: grey[800],
        main: "#151420",
        dark: grey[900]
      }
    },
    typography: {
      fontSize
    },
    breakpoints: {
      values: { xs: 0, sm: 360, md: 960, lg: 1280, xl: 1920 }
    }
  });

  const value: any = { muitheme };

  return (
    <ThemeContext.Provider value={value}>
      <MuiThemeProvider theme={muitheme}>{children}</MuiThemeProvider>
    </ThemeContext.Provider>
  );
};

export { ThemeProvider, ThemeContext };
