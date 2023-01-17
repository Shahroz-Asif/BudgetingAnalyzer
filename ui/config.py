constants = {
    "grid_size": 18,
    "x_ratio": 38,
    "y_ratio": 30,
    "x": 666, # x = x_ratio * grid_size
    "y": 540  # y = y_ratio * grid_size
}

windows = {
    "main": {
        "title": "Personalised Budgeting Analyzer"
    },
    "modify": {
        "title": "Add or Modify Purchases"
    },
    "analysis": {
        "title": "Your Budget Prediction Analysis"
    }
}

tabviews = {
    "analysis": {
        "design": {},
        "placement": {
            "row": 0,
            "column": 0,
            "padx": 1 * constants["grid_size"],
            "pady": 1 * constants["grid_size"],
            "sticky": "wnes"
        }
    }
}

menus = {
    "category": {
        "design": {},
        "placement": {
            "row": 1,
            "column": 1,
            "sticky": "we"
        }
    }
}

frames = {
    "blank": {
        "design": {
            "corner_radius": 0,
            "fg_color": "transparent"
        },
        "placement": {
            "padx": 0,
            "pady": 0,
            "sticky": "wnes"
        }
    },
    "window": {
        "design": {},
        "placement": {
            "row": 0,
            "column": 0
        }
    },
    "split": {
        "design": {
            "height": 10 * constants["grid_size"],
            "width": 10 * constants["grid_size"]
        },
        "placement": {
            "padx": 15,
            "pady": 15,
            "row": 0,
            "sticky": "wnes"
        }
    },
    "body": {
        "design": {
            "corner_radius": 1 * constants["grid_size"]
        },
        "placement": {
            "row": 1,
            "column": 0,
            "padx": 1 * constants["grid_size"],
            "pady": 1 * constants["grid_size"],
            "sticky": "wnes"
        }
    },
    "separator": {
        "design": {
            "corner_radius": 1 * constants["grid_size"],
            "height": 0.15 * constants["grid_size"]
        },
        "placement": {
            "column": 0,
            "padx": 1 * constants["grid_size"],
            "sticky": "we"
        }
    },
    "summary_category": {
        "design": {
            "corner_radius": 0.5 * constants["grid_size"],
            "width": 15 * constants["grid_size"],
            "height": 13.125 * constants["grid_size"]
        },
        "placement": {
            "row": 2,
            "column": 0,
            "padx": (0, 0.5 * constants["grid_size"]),
            "pady": (0, 0.5 * constants["grid_size"])
        }
    },
    "summary_differences": {
        "design": {
            "corner_radius": 0.5 * constants["grid_size"],
            "width": 15 * constants["grid_size"],
            "height": 13.125 *  constants["grid_size"]
        },
        "placement": {
            "padx": (0, 0.5 * constants["grid_size"]),
            "pady": (0, 0.5 * constants["grid_size"])
        }
    }
}

labels = {
    "title": {
        "design": {
            "font": ("Montserrat", 1.9 * constants["grid_size"]),
            "fg_color": "#3a7ebf",
            "corner_radius": 0.5 * constants["grid_size"],
            "padx": 10,
            "pady": 10,
            "height": 4 * constants["grid_size"]
        },
        "placement": {
            "row": 0,
            "column": 0,
            "padx": 1 * constants["grid_size"],
            "pady": (1 * constants["grid_size"], 0),
            "sticky": "wne"
        }
    },
    "subtitle": {
        "design": {
            "font": ("Montserrat", 1.4 * constants["grid_size"]),
            "fg_color": "#294967",
            "corner_radius": 0,
            "padx": 8,
            "pady": 8,
            "height": 2 * constants["grid_size"]
        },
        "placement": {
            "row": 0,
            "column": 0,
            "padx": 1 * constants["grid_size"],
            "pady": (1 * constants["grid_size"], 0),
            "sticky": "wne"
        }
    },
    "welcome": {
        "design": {
            "text": "Welcome!",
            "font": ("Arial", 2.5 * constants["grid_size"]),
            "height": 2.5 * constants["grid_size"]
        },
        "placement": {
            "row": 0,
            "column": 0,
            "columnspan": 2,
            "padx": 1 * constants["grid_size"],
            "pady": (2 * constants["grid_size"], 1 * constants["grid_size"]),
            "sticky": "wne"
        }
    },
    "small_text": {
        "design": {
            "font": ("Arial", 0.7 * constants["grid_size"])
        },
        "placement": {
            "padx": 0.5 * constants["grid_size"]
        }
    },
    "instruction": {
        "design": {
            "text": "With the help of this application, you can analyze various aspects of your spending habits in the form of graphs!",
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "wraplength": 32 * constants["grid_size"]
        },
        "placement": {
            "row": 1,
            "column": 0,
            "columnspan": 2,
            "padx": 1 * constants["grid_size"],
            "sticky": "we"
        }
    },
    "loaded": {
        "design": {
            "text": "Current Database: INTERNAL.accdb",
            "font": ("Arial", 0.6 * constants["grid_size"]),
            "wraplength": 32 * constants["grid_size"]
        },
        "placement": {
            "row": 3,
            "column": 0,
            "columnspan": 2,
            "padx": 1 * constants["grid_size"],
            "sticky": "we"
        }
    },
    "proceed": {
        "design": {
            "text": "I DO NOT have enough data to generate an analysis for you! Please Import or Add data by clicking the respective buttons above.",
            "font": ("Arial", 0.6 * constants["grid_size"]),
            "wraplength": 32 * constants["grid_size"]
        },
        "placement": {
            "row": 5,
            "column": 0,
            "columnspan": 2,
            "padx": 1 * constants["grid_size"],
            "sticky": "we"
        }
    },
    "replying": {
        "design": {
            "text": "Here's what I could do for you...",
            "font": ("Arial", 1.5 * constants["grid_size"]),
            "height": 1.5 * constants["grid_size"]
        },
        "placement": {
            "row": 0,
            "column": 0,
            "columnspan": 2,
            "padx": 1 * constants["grid_size"],
            "pady": (1 * constants["grid_size"], 0.8 * constants["grid_size"]),
            "sticky": "wne"
        }
    },
    "summary_category": {
        "design": {
            "text": "Summary by Categories",
            "font": ("Arial", 0.6 * constants["grid_size"]),
            "wraplength": 32 * constants["grid_size"]
        },
        "placement": {
            "row": 1,
            "column": 0,
            "padx": 1 * constants["grid_size"],
            "sticky": "we"
        }
    },
    "summary_differences": {
        "design": {
            "text": "Differences from previous month",
            "font": ("Arial", 0.6 * constants["grid_size"]),
            "wraplength": 32 * constants["grid_size"]
        },
        "placement": {
            "row": 1,
            "column": 1,
            "padx": 1 * constants["grid_size"],
            "sticky": "we"
        }
    },
    "component": {
        "design": {
            "font": ("Arial", 1 * constants["grid_size"])
        },
        "placement": {
            "row": 0,
            "column": 0,
            "columnspan": 2,
            "pady": (0, 0.5 * constants["grid_size"]),
            "sticky": "wne"
        }
    },
    "sort": {
        "design": {
            "font": ("Arial", 0.6 * constants["grid_size"])
        },
        "placement": {
            "row": 1,
            "column": 0,
            "padx": (0, 0.7 * constants["grid_size"]),
            "pady": (0, 0.2 * constants["grid_size"]),
            "sticky": "we"
        }
    },
    "heading": {
        "design": {
            "font": ("Arial", 0.8 * constants["grid_size"])
        },
        "placement": {
            "row": 0,
            "column": 0,
            "padx": (0, 0.8 * constants["grid_size"]),
            "pady": 0.2 * constants["grid_size"],
            "sticky": "wn"
        }
    }
}

buttons = {
    "big": {
        "design": {
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "border_spacing": 1 * constants["grid_size"],
            "width": 15 * constants["grid_size"],
            "height": 3 * constants["grid_size"]
        },
        "placement": {}
    },
    "small": {
        "design": {
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "border_spacing": 0.64 * constants["grid_size"],
            "width": 8 * constants["grid_size"],
            "height": 2 * constants["grid_size"]
        },
        "placement": {}
    },
    "import": {
        "design": {
            "text": "IMPORT ACCESS DATABASE",
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "border_spacing": 1 * constants["grid_size"],
            "width": 15 * constants["grid_size"],
            "height": 3 * constants["grid_size"]
        },
        "placement": {
            "row": 2,
            "column": 0
        }
    },
    "modify": {
        "design": {
            "text": "ADD OR MODIFY",
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "border_spacing": 1 * constants["grid_size"],
            "width": 15 * constants["grid_size"],
            "height": 3 * constants["grid_size"]
        },
        "placement": {
            "row": 2,
            "column": 1
        }
    },
    "generate": {
        "design": {
            "text": "ANALYZE!",
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "border_spacing": 1 * constants["grid_size"],
            "width": 15 * constants["grid_size"],
            "height": 3 * constants["grid_size"]
        },
        "placement": {
            "row": 6,
            "column": 0,
            "columnspan": 2
        }
    },
    "analysis": {
        "design": {
            "text": "SHOW EVERYTHING",
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "border_spacing": 0.64 * constants["grid_size"],
            "width": 12 * constants["grid_size"],
            "height": 2 * constants["grid_size"]
        },
        "placement": {
            "row": 4,
            "column": 0
        }
    },
    "download": {
        "design": {
            "text": "DOWNLOAD AS SPREADSHEET",
            "font": ("Arial", 0.8 * constants["grid_size"]),
            "border_spacing": 0.64 * constants["grid_size"],
            "width": 12 * constants["grid_size"],
            "height": 2 * constants["grid_size"]
        },
        "placement": {
            "row": 4,
            "column": 1
        }
    }
}

graphs = {
    "summary_category": {
        "placement": {
            "row": 0,
            "column": 0,
            "sticky": "wne"
        }
    },
    "summary_differences": {
        "placement": {
            "row": 0,
            "column": 0,
            "sticky": "wne"
        }
    }
}

toolbars = {
    "summary_category": {
        "placement": {
            "row": 1,
            "column": 0,
            "sticky": "wes"
        }
    },
    "summary_differences": {
        "placement": {
            "row": 1,
            "column": 0,
            "sticky": "wes"
        }
    }
}