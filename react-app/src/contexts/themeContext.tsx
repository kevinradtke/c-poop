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
  fontSize: fetchFontSize || 14,
  options: {
    type: ["light", "dark"],
    fontSize: [12, 14, 16, 18]
  }
};

const ThemeContext = createContext(initialState);

const ThemeProvider = ({ children }: { children: React.ReactNode }) => {
  const { type, fontSize } = initialState;

  const muitheme = createMuiTheme({
    palette: {
      type,
      primary: {
        light: "#38444d",
        main: "#15202b",
        dark: "#0d1217"
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
