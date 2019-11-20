import React, { createContext } from "react";
import { createMuiTheme, MuiThemeProvider } from "@material-ui/core/styles";

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
  fontSize: fetchFontSize || 16,
  options: {
    type: ["light", "dark"],
    fontSize: [12, 14, 16, 18, 20]
  }
};

const ThemeContext = createContext(initialState);

const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const { type, fontSize } = initialState;

  const muitheme = createMuiTheme({
    palette: {
      type,
      primary: {
        light: "#434957",
        main: "#282c34",
        dark: "#21252b"
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
