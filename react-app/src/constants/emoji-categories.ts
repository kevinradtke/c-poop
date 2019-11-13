interface EmojiCategories {
  [key: string]: Emoji[];
}

export interface Emoji {
  emoji: string;
  equivalentValue: string;
  shortcode: string;
}

const EMOJI_CATEGORIES: EmojiCategories[] = [
  {
    general: [
      {
        emoji: "💩",
        equivalentValue: ";",
        shortcode: ":poop:"
      }
    ]
  },
  {
    inputOutput: [
      {
        emoji: "✏️",
        equivalentValue: "print",
        shortcode: ":pencil2:"
      }
    ]
  },
  {
    variableDeclaration: [
      {
        emoji: "⬅️",
        equivalentValue: "=",
        shortcode: ":arrow_left:"
      }
    ]
  },
  {
    operators: [
      {
        emoji: "🤝",
        equivalentValue: "and",
        shortcode: ":handshake:"
      },
      {
        emoji: "👐",
        equivalentValue: "or",
        shortcode: ":open_hands:"
      },
      {
        emoji: "🙅‍♀️",
        equivalentValue: "not",
        shortcode: ":no_good:"
      },
      {
        emoji: "▶️",
        equivalentValue: ">",
        shortcode: ":arrow_forward:"
      },
      {
        emoji: "◀️",
        equivalentValue: "<",
        shortcode: ":arrow_backward:"
      },
      {
        emoji: "🙌",
        equivalentValue: "==",
        shortcode: ":raised_hands:"
      }
    ]
  },
  {
    control: [
      {
        emoji: "🤔",
        equivalentValue: "if",
        shortcode: ":thinking:"
      },
      {
        emoji: "🔁",
        equivalentValue: "while",
        shortcode: ":repeat:"
      },
      {
        emoji: "🔂",
        equivalentValue: "repeat",
        shortcode: ":repeat_one:"
      }
    ]
  },
  {
    functions: [
      {
        emoji: "🚀",
        equivalentValue: "def",
        shortcode: ":rocket:"
      },
      {
        emoji: "🤲",
        equivalentValue: "return",
        shortcode: ":palms_up:"
      },
      {
        emoji: "📭",
        equivalentValue: "void",
        shortcode: ":mailbox_with_no_mail:"
      }
    ]
  },
  {
    dataTypes: [
      {
        emoji: "💡",
        equivalentValue: "bool",
        shortcode: ":bulb:"
      },
      {
        emoji: "👍",
        equivalentValue: "True",
        shortcode: ":thumbsup:"
      },
      {
        emoji: "👎",
        equivalentValue: "False",
        shortcode: ":thumbsdown:"
      },
      {
        emoji: "🔢",
        equivalentValue: "int",
        shortcode: ":1234:"
      },
      {
        emoji: "🎈",
        equivalentValue: "float",
        shortcode: ":balloon:"
      },
      {
        emoji: "🧶",
        equivalentValue: "string",
        shortcode: ":string:"
      },
      {
        emoji: "🔤",
        equivalentValue: '"',
        shortcode: ":abc:"
      }
    ]
  }
];

export default EMOJI_CATEGORIES;
