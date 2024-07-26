return {
  "nvim-telescope/telescope-file-browser.nvim",
  dependencies = { "nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim" },
  keys = {
    "<leader>sB",
    ":Telescope file_browser path=%:p:h=%:p:h<cr>",
    desc = "Browser Files",
  },
  config = function()
    require("telescope").load_extention("file_browser")
  end,
}
