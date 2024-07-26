import { useContext } from "react"
import { pathFindingContext } from "../context/PathFindingContext"

export const usePathFinding = () => {
    const context = useContext(pathFindingContext)

    if (!context) {
        throw new Error("usePathFinding must be used within a PathFindingProviding")s
    }

    return context;
}
