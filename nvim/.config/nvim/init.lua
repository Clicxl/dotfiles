--bootstrap lazy.nvim, LazyVim and your plugins

-- Check if LazyVim is installed, if not, install it
local lazyvim_path = vim.fn.stdpath('data') .. '/lazy/lazy.nvim'

if not vim.loop.fs_stat(lazyvim_path) then
  -- Create the directory if it doesn't exist
  vim.fn.system({ 'git', 'clone', '--filter=blob:none', 'https://github.com/folke/lazy.nvim.git', lazyvim_path })
end

require("config.lazy")
