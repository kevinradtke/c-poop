import React from "react";

import { ThemeContext, ThemeProvider } from "./themeContext";

const AppProvider = ({ children }: { children: any }) => {
  return <ThemeProvider>{children}</ThemeProvider>;
};

export { AppProvider, ThemeContext };
