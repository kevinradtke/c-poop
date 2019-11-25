import React from "react";

import { CodeProvider } from "./codeContext";
import { ThemeProvider } from "./themeContext";
import { TerminalProvider } from "./terminalContext";
import { TranslatedProvider } from "./translatedContext";
import { TabsProvider } from "./tabsContext";

const AppProvider = ({ children }: { children: React.ReactNode }) => {
  return (
    <CodeProvider>
      <ThemeProvider>
        <TranslatedProvider>
          <TerminalProvider>
            <TabsProvider>{children}</TabsProvider>
          </TerminalProvider>
        </TranslatedProvider>
      </ThemeProvider>
    </CodeProvider>
  );
};

export default AppProvider;
