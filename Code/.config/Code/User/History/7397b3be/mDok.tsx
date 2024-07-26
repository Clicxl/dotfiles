import { useContext } from "react"
import { pathFindingContext } from "../context/PathFindingContext"

export const usePathfinding = () => {
    const context = useContext(pathFindingContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")s
    }

    return context;
}
