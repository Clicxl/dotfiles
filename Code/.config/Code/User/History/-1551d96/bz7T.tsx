import { useContext } from "react"
import { TileContext } from "../context/TileContext"

export const useTileContext = () => {
    const context = useContext(TileContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")
    }

    return context
}