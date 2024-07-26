return {
  "nvim-treesitter/nvim-treesitter",
  name = "treesitter",
  build = ":TSUpdate",
  config = function()
    local configs = require("nvim-treesitter.configs")
    configs.setup({
      ensure_installed = {
        "lua",
        "javascript",
        "html",
        "python",
        "rust",
        "typescript",
      },
      sync_install = true,
      auto_install = true,
      highlight = { enable = true, additonal_vim_regx_highlighting = false },
      indent = { enable = true },
    })
  end,
}
